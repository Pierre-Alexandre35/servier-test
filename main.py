# entrypoint (il prend des arguments avec la CLI, ex ENVvariables, projectID, )
from pipeline.extract import extract_input_files_to_dataframes
from pipeline.validate import process_dataframes



raw_dataframes = extract_input_files_to_dataframes('data')
print(res_list = [x[0] for x in raw_dataframes])
##cleaned_dataframes = process_dataframes(raw_dataframes)

