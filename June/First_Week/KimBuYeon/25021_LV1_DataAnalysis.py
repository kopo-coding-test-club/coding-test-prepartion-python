def solution(data, ext, val_ext, sort_by):
    column_idx = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    
    filtered_data = list(filter(lambda x : x[column_idx[ext]] < val_ext, data))
    result = sorted(filtered_data, key=lambda x : x[column_idx[sort_by]])
    return result