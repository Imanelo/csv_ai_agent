import tkinter as tk
from tkinter import filedialog, messagebox
from app.agent import CSVAIAgent

class CSVQueryApp:
    def __init__(self, root):
        self.root = root
        self.agent = None
        self._setup_ui()
        
    def _setup_ui(self):
        """Initialize GUI components"""
        self.root.title("CSV AI Analyst")
        
        # File selection section
        self.file_frame = tk.Frame(self.root)
        self.file_button = tk.Button(
            self.file_frame,
            text="1. Select CSV File",
            command=self._load_csv
        )
        self.file_label = tk.Label(self.file_frame, text="No file selected")
        
        # Query section
        self.query_frame = tk.Frame(self.root)
        self.query_label = tk.Label(self.query_frame, text="2. Enter your question:")
        self.query_entry = tk.Text(self.query_frame, height=3, width=50)
        
        # Process button
        self.process_button = tk.Button(
            self.root,
            text="3. Analyze Data",
            command=self._process_query,
            bg="#4CAF50",  # Green color
            fg="white"
        )
        
        # Results display
        self.result_text = tk.Text(self.root, height=15, width=60)
        
        # Layout using grid
        self.file_frame.pack(pady=10, fill=tk.X)
        self.file_button.pack(side=tk.LEFT, padx=5)
        self.file_label.pack(side=tk.LEFT)
        
        self.query_frame.pack(pady=10, fill=tk.X)
        self.query_label.pack(anchor=tk.W)
        self.query_entry.pack()
        
        self.process_button.pack(pady=10)
        self.result_text.pack(pady=10, fill=tk.BOTH, expand=True)

    def _load_csv(self):
        """Handle CSV file loading"""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.agent = CSVAIAgent(file_path)
                self.file_label.config(text=file_path)
                messagebox.showinfo("Success", "CSV file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def _process_query(self):
        """Handle query processing"""
        if not self.agent:
            messagebox.showwarning("Warning", "Please select a CSV file first!")
            return
            
        question = self.query_entry.get("1.0", tk.END).strip()
        if not question:
            messagebox.showwarning("Warning", "Please enter a question!")
            return
            
        try:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Analyzing...\n")
            self.root.update()  # Force UI update
            
            result = self.agent.query(question)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Result:\n{'-'*40}\n{result}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = CSVQueryApp(root)
    root.mainloop()