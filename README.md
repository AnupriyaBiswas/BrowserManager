Problem Description

To create a console-based application that simulates the history management functionality of a Web-Browser using a Doubly-Linked List. The program will allow users to visit new pages, go back to the previous page, move forward, and view the history.
Key Features : 
1.	Visit a New Page:
a.	Simulate visiting a new web page, which adds the page to the history.
b.	When  a new page is visited, if there were any “forward” pages, they should be removed (similar to how real browsers work when you navigate after going back).

1.	Go Back:
a.	Move back to the previous page in the history.
b.	Ensure that the user can’t go back if they’re at the first page in the history.

2.	Display Playlist:
a.	Display the entire Playlist showing the song's position, title, artist and duration.
b.	Optionally, display the total duration of all songs

3.	Go forward:
a.	Move forward to the next page in the history(if available)
b.	Ensure that that the user can’t go back if they’re at the most recent page.

4.	View History:
a.	Display the complete browsing history from the first visited page to the current page.
b.	Indicate the current page the user is on.

5.	Clear History:
a.	Clear all the History, starting fresh as if the browser was just opened.

Technical Details:
1.	Data Structure: 
a.	Use a Doubly-Linked List to represent the browsing history. Each node in the list will represent a web page, containing the URL and pointers/references to both the previous and next pages.

2.	Classes and Methods:
a.	Page Class: To store details of each visited Page, such as the URL.
b.	History Class: To manage the doubly-linked list of pages with methods like 'visitPage', 'goBack', 'goForward', 'viewHistory', and 'clearHistory'.

3.	Operations:
a.	Add Node: When a new page is visited, add it to the end of the list and adjust pointers.
b.	Traverse List Backward/Forward: Implement Functionality to move back and forth through the list.
c.	Delete Node: When visiting a new page after going back, remove all forward nodes.

Advanced Features:
1.	Bookmark Pages: Allow users to bookmark specific pages so they can jump directly to them later.
2.	Search History: Implement a search feature that allows users to find a specific page in their history by URL or title.
3.	Undo/Redo Navigation: Add functionality to undo and redo navigational actions.
4.	Graphical Interface: Create a simple GUI to make the history navigation more intuitive, using tools like Tkinter(Python) or JavaFX.

Language and Tools:
1.	Programming Language: Python
2.  Text Editor: VS Code
2. 
