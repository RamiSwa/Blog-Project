

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

Now git checkout -b main-2
