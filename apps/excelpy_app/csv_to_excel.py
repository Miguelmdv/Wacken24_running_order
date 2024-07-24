import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
from file_paths import RUN_ORD_MERGED_FILE, EXCEL_FILE


def run():
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(RUN_ORD_MERGED_FILE)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel(EXCEL_FILE, index=False)

    # Cargar el archivo Excel para darle formato de tabla
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active

    # Crear una tabla en la hoja de trabajo
    tab = Table(displayName="Table1", ref=f"A1:{ws.dimensions.split(':')[1]}")

    # Añadir estilo a la tabla
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                        showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style


    # Añadir la tabla a la hoja de cálculo
    ws.add_table(tab)
    
    # Ajustar el ancho de las columnas
    for column_cells in ws.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = length

    # Guardar el archivo Excel con el formato de tabla
    wb.save(EXCEL_FILE)

    print(f"\nEl archivo '{RUN_ORD_MERGED_FILE.name}' ha sido convertido a Excel y guardado como '{EXCEL_FILE}'.")

