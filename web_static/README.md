Introduction to HTML & CSS
This is a guide to get you started with the building blocks of the web: HTML and CSS!

What is HTML?

HTML stands for HyperText Markup Language. It's the foundation of web pages, providing the structure and content.  Imagine HTML as the skeleton of a webpage, defining headings, paragraphs, images, and other elements.

How to Create an HTML Page:

Here's the basic structure of an HTML page:

HTML
<!DOCTYPE html>
<html>
<head>
  <title>Your Page Title</title>
</head>
<body>
  </body>
</html>

You can create an HTML file using any text editor (like Notepad) and save it with a .html extension.

Markup Language Explained:

A markup language like HTML uses tags to define the structure and meaning of content within a plain text document. These tags are instructions for the web browser on how to display the content.

What is the DOM (Document Object Model):

The Document Object Model (DOM) is a tree-like representation of an HTML document. The browser creates this DOM when it loads a webpage.  The DOM allows you to interact with and manipulate the webpage content using scripting languages like JavaScript.

Elements and Tags:

The building blocks of HTML are elements, which are represented by opening and closing tags (<tag> and </tag>). Elements define the different parts of your webpage content, like headings (<h1>), paragraphs (<p>), images (<img>), etc.

What are Attributes:

Attributes provide additional information about an element.  For example, an <img> tag might have a src attribute that specifies the image source file.

How the Browser Loads a Webpage:

Request: When you enter a URL in the address bar, the browser sends a request to the web server for that webpage.
Response: The web server responds by sending the HTML code for the webpage.
Parsing: The browser parses the HTML code, creating the DOM tree.
Rendering: The browser uses the DOM and CSS (if provided) to render the webpage on the screen.
What is CSS?

Cascading Style Sheets (CSS) define the presentation of an HTML document. It's like adding the flourishes to your webpage's skeleton (HTML) with styles like fonts, colors, layouts, etc.

Adding Style to an Element:

You can add styles to elements using CSS selectors and style declarations. Selectors target specific elements, and style declarations define the properties you want to change (e.g., color: red;).

What are Classes:

Classes are a way to group similar elements and apply the same styles to them. You can assign a class name (e.g., .important) to elements in your HTML, and then target that class in your CSS to define styles.

Understanding Selectors:

Selectors are patterns that tell the browser which elements to style.  There are different types of selectors, like element type selectors (p), class selectors (.important), and ID selectors (#unique-id).

Calculating CSS Specificity:

Specificity determines which CSS rule applies to an element when multiple rules target it.  It's based on a point system considering factors like IDs, classes, and element types.

Box Model in CSS:

The box model is a way to visualize how CSS styles elements on a webpage. It considers the following properties of an element:

Content: The actual content within the element, like text or images.
Padding: The transparent area around the content that creates space between the content and the border.
Border: The decorative line around the padding and content (optional).
Margin: The transparent area outside the border that creates space between the element and other elements.
These properties are applied cumulatively to define the overall size and position of the element on the webpage.

Here's a visual representation of the box model:

  +----------------+
  |     Margin     |
  +----------------+
  | Padding        |
  |   +------------+   |
  |   | Content   |   |
  |   +------------+   |
  | Padding        |
  +----------------+
  |     Margin     |
  +----------------+
By understanding and manipulating these properties in CSS, you can achieve different design layouts for your webpages.