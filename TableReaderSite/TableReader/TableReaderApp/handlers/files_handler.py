import pandas as pd
import io


def to_excel_tabel(tabs: list):
    pd_tabs = []
    for tab in tabs:
        pd_tabs.append(pd.DataFrame.from_dict(data=tab))
    buff = io.BytesIO()
    with pd.ExcelWriter(buff) as writer:
        for idx, tab in enumerate(pd_tabs):
            tab.to_excel(writer, sheet_name=f'Sheet {idx}')
    return buff



