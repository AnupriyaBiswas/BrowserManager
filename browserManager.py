import tkinter as tk
from tkinter import messagebox, ttk

class Page:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class History:
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None
        self.bookmarks = []
        self.undo_stack = []
        self.redo_stack = []

    def visit_page(self, url):
        new_page = Page(url)
        if self.current:
            # Clear forward history
            self.current.next = None
            self.redo_stack.clear()  # Clear redo stack on new visit
        new_page.prev = self.current
        if self.current:
            self.current.next = new_page
        
        self.current = new_page
        if not self.head:
            self.head = new_page
        self.tail = new_page if not new_page.next else self.tail
        self.undo_stack.append("visit")
        self.view_history()
        return url
    

    def go_back(self):
        if self.current and self.current.prev:
            self.redo_stack.append(self.current.url)  # Save current page for redo
            self.current = self.current.prev
            self.undo_stack.append("back")
            return self.current.url
        else:
            return "No previous pages."

    def go_forward(self):
        if self.current and self.current.next:
            self.undo_stack.append("forward")
            self.current = self.current.next
            return self.current.url
        else:
            return "No next pages."

    def view_history(self):
        history = []
        page = self.head
        while page:
            history.append(f"{page.url} (Current)" if page == self.current else page.url)
            page = page.next
        return "\n".join(history)

    def clear_history(self):
        self.head = None
        self.current = None
        self.tail = None
        self.bookmarks.clear()
        self.undo_stack.clear()
        self.redo_stack.clear()
        return "History cleared."

    def bookmark_page(self):
        if self.current and self.current.url not in self.bookmarks:
            self.bookmarks.append(self.current.url)
            return f"Bookmarked: {self.current.url}"
        return "Already bookmarked."

    def view_bookmarks(self):
        return "\n".join(self.bookmarks) if self.bookmarks else "No bookmarks."

    def search_history(self, keyword):
        results = []
        page = self.head
        while page:
            if keyword.lower() in page.url.lower():
                results.append(page.url)
            page = page.next
        return "\n".join(results) if results else "No matches found."

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            if action == "visit" and self.current.prev:
                self.redo_stack.append(self.current.url)
                self.current = self.current.prev
                return f"Undo to: {self.current.url}"
            elif action == "back" and self.current.next:
                self.current = self.current.next
                return f"Undo to: {self.current.url}"
        return "Nothing to undo."

    def redo(self):
        if self.redo_stack:
            next_page = self.redo_stack.pop()
            self.visit_page(next_page)
            return f"Redo to: {next_page}"
        return "Nothing to redo."

# GUI setup
def main():
    history = History()
    
    # Create main window
    root = tk.Tk()
    root.title("Browser History Manager")

    # Open window in maximized mode
    root.state("zoomed")  # Works on Windows and some other OSes

    # History Text Box
    history_label = tk.Label(root, text="Browsing History", font=("Arial", 14))
    history_label.pack()
    history_text = tk.Text(root, height=10, width=5, state=tk.DISABLED)
    history_text.pack(fill=tk.BOTH, expand=True)

    # Function to update the history text box
    def update_history():
        history_text.config(state=tk.NORMAL)
        history_text.delete("1.0", tk.END)
        history_text.insert(tk.END, history.view_history())
        history_text.config(state=tk.DISABLED)

    # Bookmark Text Box
    bookmark_label = tk.Label(root, text="Bookmarks", font=("Arial", 14))
    bookmark_label.pack()
    bookmark_text = tk.Text(root, height=10, width=5, state=tk.DISABLED)
    bookmark_text.pack(fill=tk.BOTH, expand=True)

    # Function to update the bookmarks text box
    def update_bookmarks():
        bookmark_text.config(state=tk.NORMAL)
        bookmark_text.delete("1.0", tk.END)
        bookmark_text.insert(tk.END, history.view_bookmarks())
        bookmark_text.config(state=tk.DISABLED)

    # Visit a new page
    def visit_page(event=None):
        url = url_entry.get()
        if url:
            history.visit_page(url)
            update_history()
            url_entry.delete(0, tk.END)

    # Go back
    def go_back():
        result = history.go_back()
        update_history()
        messagebox.showinfo("Go Back", result)

    # Go forward
    def go_forward():
        result = history.go_forward()
        update_history()
        messagebox.showinfo("Go Forward", result)

    # Clear history
    def clear_history():
        result = history.clear_history()
        update_history()
        messagebox.showinfo("Clear History", result)

    # Bookmark the current page
    def bookmark_page():
        result = history.bookmark_page()
        update_bookmarks()
        messagebox.showinfo("Bookmark Page", result)

    # Search history
    def search_history():
        keyword = search_entry.get()
        results = history.search_history(keyword)
        messagebox.showinfo("Search Results", results)

    # Undo action
    def undo_action():
        result = history.undo()
        update_history()
        messagebox.showinfo("Undo Action", result)

    # Redo action
    def redo_action():
        result = history.redo()
        update_history()
        messagebox.showinfo("Redo Action", result)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12, "bold"), foreground="#4CAF50")

    button_frame = tk.Frame(root)
    button_frame.pack()
    for i in range(5):
        button_frame.columnconfigure(i, weight=1)


    # URL Entry
    url_entry = tk.Entry(root, width=80)
    url_entry.pack(pady=10, padx=10)
    url_entry.bind("<Return>", lambda event: visit_page())

    # Button Frame Setup
    button_frame = tk.Frame(root)
    button_frame.pack()
    for i in range(5):
        button_frame.columnconfigure(i, weight=1)  # Equal width for columns

    # Visit Page Button
    visit_button = ttk.Button(button_frame, text="Visit Page", command=visit_page)
    visit_button.grid(row=0, column=0)

    # Navigation Buttons
    back_button = ttk.Button(button_frame, text="Go Back", command=go_back)
    back_button.grid(row=0, column=1)

    forward_button = ttk.Button(button_frame, text="Go Forward", command=go_forward)
    forward_button.grid(row=0, column=2)

    clear_button = ttk.Button(button_frame, text="Clear History", command=clear_history)
    clear_button.grid(row=0, column=3)

    # Bookmark Button
    bookmark_button = ttk.Button(button_frame, text="Bookmark Page", command=bookmark_page)
    bookmark_button.grid(row=0, column=4)


    # Search Entry and Search Button
    search_entry = ttk.Entry(root, width=80)
    search_entry.pack(pady=10, padx=10)

    #Undo and Redo Button# Undo and Redo Frame
    undo_redo_search_frame = ttk.Frame(root)
    undo_redo_search_frame.pack()

    # Configure columns for equal width
    undo_redo_search_frame.columnconfigure(0, weight=1)
    undo_redo_search_frame.columnconfigure(1, weight=1)
    undo_redo_search_frame.columnconfigure(2, weight=1)

    # Undo and Redo Buttons in the same row
    search_button = ttk.Button(undo_redo_search_frame, text = "Search History", command=search_history)
    search_button.grid(row=0, column=0)

    undo_button = ttk.Button(undo_redo_search_frame, text="Undo", command=undo_action)
    undo_button.grid(row=0, column=1)

    redo_button = ttk.Button(undo_redo_search_frame, text="Redo", command=redo_action)
    redo_button.grid(row=0, column=2)


    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
