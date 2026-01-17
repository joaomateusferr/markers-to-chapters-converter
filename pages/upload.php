<form action="index.php" method="post" enctype="multipart/form-data">
    <div class="row"><h1>Upload your markes CSV file</h1></div>
    <div class="row justify-content-center">
        <div class="col-md-12">
            <input type="file" name="csv" id="csv" accept=".csv,text/csv" required>
        </div>
    </div>
    <div class="row justify-content-center">
        <div class="col-md-4">
            <button type="submit" id="submit-btn" disabled>Process</button>
        </div>
    </div>
</form>

<script>

    const input = document.getElementById('csv');
    const submitBtn = document.getElementById('submit-btn');

    input.addEventListener('change', () => {

        if (input.files.length > 0) {
            submitBtn.disabled = false;
        } else {
            submitBtn.disabled = true;
        }

    });

</script>