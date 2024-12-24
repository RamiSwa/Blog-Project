

---

**Blog Project - Full Stack Django Blog with AI Integration**

This is a full-stack blog application built using Django, Bootstrap 5, and integrated with AI features for enhanced user experience. The project allows users to create, view, and interact with blog posts, while also including features for liking and disliking posts and comments.

Key features of the blog project:
- **Django Backend**: Utilizes Django for the backend to manage posts, categories, comments, and user authentication.
- **AI Integration**: Future features include personalized recommendations based on AI algorithms to improve user engagement and provide a personalized blog reading experience.
- **Bootstrap 5**: The front-end is styled using Bootstrap 5 for a responsive and modern UI, with a focus on a seamless user experience across devices.
- **Comment System**: Allows users to comment on posts, with an approval workflow for administrators.
- **Like/Dislike System**: Users can interact with posts and comments using a like/dislike system.
- **Admin Panel**: Fully functional Django admin interface to manage posts, comments, users, and other data.
- **Pagination**: Posts are displayed in a paginated manner to improve user navigation.

**Technologies Used**:
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (for development) or PostgreSQL (for production)
- **Additional Tools**: CKEditor for rich text editing, AJAX for dynamic interaction, CSRF protection

---

To upload your project to the new GitHub repository, follow these steps:

### 1. **Initialize Git in your project directory:**
   Open your terminal (or command prompt) and navigate to your project directory using the `cd` command:

   ```bash
   cd path/to/your/project
   ```

   Then, initialize Git by running:

   ```bash
   git init
   ```

### 2. **Add your project files to Git:**
   Add all the files in your project directory to Git with the following command:

   ```bash
   git add .
   ```

   This stages all files for commit.

### 3. **Commit your changes:**
   Now, commit the files to Git with a message:

   ```bash
   git commit -m "Initial commit"
   ```

### 4. **Add your GitHub repository as a remote:**
   Next, you need to link your local project with the GitHub repository you created. Run this command, replacing the URL with your GitHub repository URL:

   ```bash
   git remote add origin https://github.com/RamiSwa/Blog-Project.git
   ```

### 5. **Push your code to GitHub:**
To create a new branch in Git and push it to your GitHub repository, follow these steps:

### 1. **Create a new branch:**
   To create a new branch, use the following command (replace `new-branch-name` with your desired branch name):

   ```bash
   git checkout -b main-1
   ```

   This command does two things:
   - Creates a new branch named `main-1`.
   - Switches to that branch.

### 2. **Push the new branch to GitHub:**
   After creating and switching to your new branch, push it to GitHub with the following command:

   ```bash
   git push -u origin main-1
   ```

   This will push the new branch to your GitHub repository and set it as the upstream branch, meaning future `git push` commands will automatically push changes to this branch.

### 3. **Verify the branch on GitHub:**
   - Go to your GitHub repository.
   - Click the **Branch** dropdown (where it says `main`).
   - You should see the new branch (`main-1`) listed there.

---

### 4. **Switch back to the `main` branch (if needed):**
   If you want to switch back to the `main` branch (or any other branch), you can use:

   ```bash
   git checkout main
   ```

---

### 5. **Push changes to your new branch:**
   If you make any changes on your new branch and want to commit them, use the following steps:

   - Stage the changes:
     ```bash
     git add .
     ```
   - Commit the changes:
     ```bash
     git commit -m "Your commit message"
     ```
   - Push the changes to GitHub:
     ```bash
     git push
     ```

---

### Summary:
1. Create a new branch: `git push --set-upstream origin main-1`
2. Push it to GitHub: `git push -u origin maim-1`
3. Make changes and commit them as usual, then push them to the new branch.

   This will upload your project to GitHub.

![image](https://github.com/user-attachments/assets/835ace52-3ef4-4807-b759-43d47002f8ee)

![image](https://github.com/user-attachments/assets/25c6956b-40e1-4440-abc6-fa635b865693)

---------------------------------------------------------------------------------------------------


---

### **Blog Project - Summary of Steps**

1. **Project Setup:**
   - Created a Django project and app for the Blog.
   - Installed and set up necessary dependencies, including `django-ckeditor` for rich text editing.

2. **Models:**
   - Defined models for **Post**, **Category**, **Tag**, and **Comment** in `models.py`.
   - Implemented relationships between models: 
     - **Many-to-many** between **Post** and **Category**/**Tag**.
     - **Foreign key** relationships for **Post** and **Comment**.
   - Added fields like `slug`, `image`, `status`, `likes`, and `dislikes` for Posts and Comments.
   - Included methods for like/dislike counts and related posts.

3. **Admin Configuration:**
   - Customized the Django Admin interface to manage **Categories**, **Tags**, **Posts**, and **Comments**.
   - Added actions in the Admin panel, such as approving comments and marking posts as published.
   - Displayed like and dislike counts in the Post Admin.

4. **Forms:**
   - Created forms for **Post** creation and editing (PostForm) and for submitting **Comments** (CommentForm).
   - Styled form fields using Bootstrap classes.

5. **Views:**
   - Created views to handle:
     - Displaying the **home** page with paginated posts.
     - **Post details** page with related posts, comments, and the ability to add comments.
     - Filtering posts by **Category** and **Tag**.
     - Liking and disliking posts via AJAX requests.
   - Implemented functionality to increment post views and manage comment submissions.

6. **URLs:**
   - Defined URL routes to handle different pages, including post detail, category, tag, and like/dislike functionality.

7. **AJAX (Like/Dislike):**
   - Implemented AJAX-based views to toggle likes and dislikes on posts and update the count without reloading the page.


8. **HTML Templates Overview:**

8.1. **Base Template (`base.html`):**
   - This is the foundational template that all other templates extend.
   - It includes common elements such as:
     - Bootstrap CSS and JS for styling and responsiveness.
     - A navigation bar with links to home and other pages.
     - A section for custom content using `{% block content %}`.
     - Static and media file links for styling and image handling.
   - External libraries like Bootstrap Icons and jQuery are included for additional functionality and UI.

8.2. **Home Page Template (`home.html`):**
   - Displays a list of **latest posts** in a grid layout.
   - Each post shows the title, image, and a truncated version of its content.
   - Includes pagination for navigating through posts.
   - Provides a link to each post’s detail page.

8.3. **Post Detail Page Template (`post_detail.html`):**
   - Displays detailed content of a single post, including:
     - Post title, image, publish date, and author.
     - Full post content.
     - Like and Dislike buttons with AJAX functionality to update the like/dislike count.
   - A comment section where users can:
     - See existing comments.
     - Add new comments if they are authenticated.
     - Wait for admin approval if the comment is pending.
   - Displays **related posts** based on the current post’s category or tags.

8.4. **Category Posts Page Template (`category_posts.html`):**
   - Displays all posts in a specific category.
   - Lists each post with its title and image, and a "Read More" button leading to the detailed post page.
   - If no posts are available in the category, a message is displayed to inform the user.

---

### **Settings for Static and Media Files**

- **Static Files Configuration:**
  - `STATIC_URL`: URL path for serving static files.
  - `STATICFILES_DIRS`: Points to the `static` directory for custom static files like CSS and JavaScript.

- **Media Files Configuration:**
  - `MEDIA_URL`: URL path for serving user-uploaded files (e.g., post images).
  - `MEDIA_ROOT`: The directory where uploaded files will be stored locally.

---

### **AJAX Functionality in `post_detail.html`**

- The **Like** and **Dislike** buttons have been set up to trigger AJAX requests. When clicked:
  - The count for likes or dislikes is updated dynamically on the page.
  - The AJAX requests are handled by corresponding Django views, which update the like/dislike counts in the database.

---

### **Setup Instructions**
1. Clone the repository to your local machine.
2. Install the dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.

---

After this Go to git checkout -b main-2
