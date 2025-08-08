import os

folder_path = r"C:\Users\rajmd\OneDrive\Desktop\ASD\Assignments\PYTHON\Assignment5"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt") and not filename.startswith("processed_"):
        old_path = os.path.join(folder_path,filename)
        new_filename = f"processed_{filename}"
        new_path=os.path.join(folder_path,new_filename)
        
        os.rename(old_path,new_path)
        print(f"Renamed:{filename}->{new_filename}")

print("Renaming done")

# Renamed:cleaned_data.txt->processed_cleaned_data.txt
# Renamed:data.txt->processed_data.txt
# Renaming done