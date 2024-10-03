### Using `pip` and `venv`

#### Step 1: Create a Virtual Environment

1. **Open your terminal (or command prompt)**.
2. **Navigate to your project directory** or create a new one:

   ```bash
   mkdir myproject
   cd myproject
   ```

3. **Create a virtual environment** named `venv` (or any name you prefer):

   ```bash
   python -m venv venv
   ```

   This will create a new directory named `venv` that contains a copy of the Python interpreter, the standard library, and various supporting files.

#### Step 2: Activate the Virtual Environment

- **On Windows**:

   ```bash
   venv\Scripts\activate
   ```

- **On macOS/Linux**:

   ```bash
   source venv/bin/activate
   ```

After activation, your terminal prompt will change to indicate that you are now working within the virtual environment.

#### Step 3: Install Packages with `pip`

Now that the virtual environment is active, you can install packages using `pip`. For example:

```bash
pip install fastapi
```

You can install multiple packages at once:

```bash
pip install fastapi uvicorn
```

#### Step 4: Freeze Dependencies

To keep track of the installed packages and their versions, you can create a `requirements.txt` file. This can be done by running:

```bash
pip freeze > requirements.txt
```

This command will list all installed packages and their versions in a file named `requirements.txt`. This file can be shared with others or used for deployment.

#### Step 5: Install Dependencies from `requirements.txt`

If someone else needs to set up the project or if you need to set it up on another machine, you can install all dependencies listed in `requirements.txt` with:

```bash
pip install -r requirements.txt
```

#### Step 6: Deactivating the Virtual Environment

To exit the virtual environment, simply run:

```bash
deactivate
```

Your terminal prompt will return to normal, and you’ll be back in your system’s Python environment.

### Summary

Using `pip` with `venv` is a straightforward and effective way to manage Python projects. Here’s a recap of the steps:

1. **Create a project directory**.
2. **Create a virtual environment** using `venv`.
3. **Activate the virtual environment**.
4. **Install packages using `pip`**.
5. **Freeze dependencies** to a `requirements.txt` file.
6. **Install from `requirements.txt`** when needed.
7. **Deactivate the environment** when done.