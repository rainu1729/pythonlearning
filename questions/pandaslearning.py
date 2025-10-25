import pandas as pd

def consecutive_number (logs: pd.DataFrame) -> pd.DataFrame:
    
    result = set()
    consecNumbertoCheck = 3
    itr = 0
    fillerNumber = -99
    print(len(logs))

    if len(logs) < consecNumbertoCheck:
        return  pd.DataFrame(result, columns=['ConsecutiveNums'])

    series  = pd.Series(logs['num'])
    temp_df = pd.DataFrame()

    while itr < consecNumbertoCheck:
        #append right
        temp_ser = series if itr == 0 else pd.concat([series, pd.Series([fillerNumber] * itr)], ignore_index=True)
        #append left
        temp_ser = temp_ser if (consecNumbertoCheck-itr-1) == 0 else pd.concat([pd.Series([fillerNumber] * (consecNumbertoCheck-itr-1)) , temp_ser], ignore_index=True)
        temp_df['ser_'+str(itr)]=temp_ser
        itr +=1

    dft = temp_df.T

    for column_name in dft.columns:
        
        ele = dft[column_name].iloc[0] if (dft[column_name] == dft[column_name].iloc[0]).all() else None
        
        if ele is not None:
            result.add(ele)

    return pd.DataFrame(result, columns=['ConsecutiveNums'])


if __name__ == "__main__":
    data =pd.DataFrame({'id': [1,2,3,4,5,6,7,8,9],
        'num': [1, 1, 1,2,3,4,5,6,9]})
    val = consecutive_number(data)

    print(val)


