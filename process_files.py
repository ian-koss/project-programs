# process_files.py
import os

folder_path = r'C:\Users\Herob\Documents\test_folder'
prefix = 'processed_'

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        old_path = os.path.join(folder_path, filename)
        new_filename = prefix + filename
        new_path = os.path.join(folder_path, new_filename)
        
        # Read the original file
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process the content (convert to uppercase)
        processed_content = content.upper()
        
        # Write to the new file
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f'Processed: {filename} -> {new_filename}')