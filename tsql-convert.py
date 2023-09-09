import re
import os


def translate_tsql_to_simple(query):
    # Match database.schema.table and use non-capturing groups (?:...) for parts we don't want to replace
    pattern = r'((?:[\s(]|^)\w+)\.\w+\.(\w+(?:[\s,);]|$))'
    translated_query = re.sub(pattern, r'\1.\2', query)
    return translated_query


def translate_tsql_to_complex(query, default_schema="dbo"):
    # Match database.table and use non-capturing groups for parts we don't want to replace
    pattern = r'((?:[\s(]|^)\w+)\.(\w+(?:[\s,);]|$))'
    translated_query = re.sub(pattern, r'\1.' + default_schema + r'.\2', query)
    return translated_query


def process_sas_file(input_file_path, output_folder, translation_mode="simple"):
    with open(input_file_path, 'r') as file:
        content = file.read()

    if translation_mode == "simple":
        translated_content = translate_tsql_to_simple(content)
    elif translation_mode == "complex":
        translated_content = translate_tsql_to_complex(content)
    else:
        raise ValueError("Invalid translation mode!")

    # Make sure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write to a new .sas file in the output folder
    output_file_path = os.path.join(
        output_folder, os.path.basename(input_file_path))
    with open(output_file_path, 'w') as file:
        file.write(translated_content)

    print(
        f"Processed {input_file_path}. Translated file saved to {output_file_path}")


def process_sas_files_in_folder(input_folder, output_folder, translation_mode="simple"):
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.sas'):
            input_file_path = os.path.join(input_folder, file_name)
            process_sas_file(input_file_path, output_folder, translation_mode)


input_folder_path = './original-sas-code'
output_dir = './modified-sas-code'
process_sas_files_in_folder(
    input_folder_path, output_dir, translation_mode="simple")
