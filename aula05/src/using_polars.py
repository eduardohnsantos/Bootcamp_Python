import polars as pl

def create_polars_df():
    # Aumenta o tamanho do chunk para ler grandes volumes de dados de forma eficiente
    pl.Config.set_streaming_chunk_size(4000000)
    
    return (
        # 1. Lemos 'measure' como String temporariamente para evitar quebras no parser do CSV
        pl.scan_csv(
            "data/measurements.txt", 
            separator=";", 
            has_header=False, 
            new_columns=["station", "measure"], 
            schema={"station": pl.String, "measure": pl.String}
        )
        # 2. Tratamento de dados: substitui vírgulas por pontos e converte para Float64.
        # O uso de strict=False impede que linhas mal formatadas quebrem o script (viram Null).
        .with_columns(
            pl.col("measure")
            .str.replace(",", ".", literal=True)
            .cast(pl.Float64, strict=False)
        )
        # 3. Remove eventuais linhas nulas/inválidas para não afetar os cálculos
        .drop_nulls("measure")
        # 4. Agrupamento e agregações
        .group_by("station") 
        .agg([
            pl.col("measure").max().alias("max"),
            pl.col("measure").min().alias("min"),
            pl.col("measure").mean().alias("mean")
        ])
        .sort("station")
        .collect(engine="streaming")
    )

if __name__ == "__main__":
    import time

    print("Iniciando o processamento com Polars...")
    start_time = time.time()
    df = create_polars_df()
    took = time.time() - start_time
    
    print(df)
    print(f"Polars Took: {took:.2f} sec")