# build_lambda_package.ps1

# Cleanup
$zipName = "lambda_deploy.zip"
$packageDir = "lambda_package"

Remove-Item $packageDir -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item $zipName -Force -ErrorAction SilentlyContinue

# Step 1: Create clean folder
New-Item -ItemType Directory -Force -Path $packageDir

# Step 2: Install required packages
pip install transformers==4.40.1 --target $packageDir
pip install boto3 --target $packageDir
pip install pdfplumber --target $packageDir
pip install pillow --target $packageDir        # required by pdfplumber
pip install pdf2image --target $packageDir     # required for OCR fallback
pip install pytesseract --target $packageDir   # OCR engine wrapper

# Step 3: Copy source code
Copy-Item lambda_function.py -Destination $packageDir
Copy-Item -Recurse src -Destination $packageDir

# Step 4: Zip it
Compress-Archive -Path "$packageDir\*" -DestinationPath $zipName

Write-Host "`n✅ Lambda ZIP package created: $zipName"
