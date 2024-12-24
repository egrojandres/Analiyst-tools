class file:
           
    def dict_organize(self):
        with open("Vocabulary.txt", 'r') as file: # Read all lines into a list lines = file.readlines()
            lines = file.readlines()
        lines = [line.strip() for line in lines]            
        lines.sort(key=lambda x: x.lower())
        
        with open("Vocabulary.txt", 'w') as file:
            # Write each sorted line back to the file with a newline character 
            for line in lines:
                file.write(line + "\n")

if __name__ == '__main__':
    File = file()
    File.dict_organize()