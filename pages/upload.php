<form action="index.php" method="post" enctype="multipart/form-data">

    <h1>Send your markers CSV file</h1>

    <input type="file" name="csv" id="csv" accept=".csv,text/csv" required>
    <label for="csv">Select file</label>
    <div class="file-name" id="file-name">No file selected</div>

    <div class="actions">
        <button type="submit" id="submit-btn" disabled>Process</button>
    </div>

</form>

<script>

    const input = document.getElementById('csv');
    const fileName = document.getElementById('file-name');
    const submitBtn = document.getElementById('submit-btn');

    input.addEventListener('change', () => {

        if (input.files.length > 0) {

            fileName.textContent = "Selected file: " + input.files[0].name;
            submitBtn.disabled = false;

        } else {

            fileName.textContent = "No file selected";
            submitBtn.disabled = true;

        }

    });

</script>