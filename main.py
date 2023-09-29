# API Key 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
import openai
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def generate_file():
    input_text = prompt_text.get("1.0", tk.END)
    # Add your OpenAI code to generate a new file based on input_text and uploaded file

def locate_generated_file():
    # Add your code to locate the generated file and open its folder
    pass
def open_settings():
    # Add code to open the settings window here
    pass

def open_about():
    # Add code to open the about window here
    pass
# Create the main window
root = tk.Tk()
root.title("OpenAI File Generator")
root.geometry("500x400")
root.configure(bg="#F4FDCE")
#Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="Settings", menu=file_menu, command=open_settings())
menu_bar.add_cascade(label="About", menu=file_menu, command=open_about())

# Create a frame for the main content
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)
# Create a frame for the file upload section
file_frame = tk.Frame(root)
file_frame.pack(pady=20)

upload_button = tk.Button(file_frame, text="Upload File", command=upload_file)
upload_button.pack(side=tk.LEFT)
file_entry = tk.Entry(file_frame, width=40)

file_entry.pack(side=tk.LEFT)

# Create a text area for input prompt
prompt_label = tk.Label(root, text="Enter Prompt:")
prompt_label.pack()
prompt_text = tk.Text(root, width=50, height=10)
prompt_text.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="Generate File", command=generate_file)
generate_button.pack(side=tk.LEFT)

locate_button = tk.Button(button_frame, text="Locate Generated File", command=locate_generated_file)
locate_button.pack(side=tk.LEFT)

# Create a progress bar (you can update this as your OpenAI code progresses)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(pady=0)

root.mainloop()





















'''
# Set your OpenAI API key
openai.api_key = "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"
# Read the contents of input.txt
with open("input.txt", "r") as input_file:
    input_text = input_file.read()

# Define your prompt
prompt = f"Generate a one-third summary of input.txt:\n\n{input_text}"

# Make an API request
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=150,  # Adjust the max tokens based on your needs.
)

# Extract the generated text
generated_text = response.choices[0].text

# Save the generated text to output.txt
with open("output.txt", "w") as output_file:
    output_file.write(generated_text)
'''