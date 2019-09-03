# Download and Read Barcode Images
Use Python to download barcode images from Google and read barcodes with [Dynamsoft Barcode Reader](https://www.dynamsoft.com/Products/Dynamic-Barcode-Reader.aspx).

## Usage
Install [google-images-download](https://github.com/hardikvasa/google-images-download):

```
pip install google_images_download
```

Install [Python barcode extension](https://github.com/dynamsoft-dbr/python) built with Dynamsoft Barcode Reader.

Get a [free trial license](https://www.dynamsoft.com/CustomerPortal/Portal/Triallicense.aspx) of Dynamsoft Barcode Reader and set the `'LICENSE-KEY'` in ``app.py``:

```python
dbr.initLicense('LICENSE-KEY')
```

Set a keyword:

```python
keyword = "barcode on box"
```

Run the app:

```
python app.py
```

![download read barcode image](https://www.codepool.biz/wp-content/uploads/2019/09/download-read-barcode-image.png)

## Reference
https://google-images-download.readthedocs.io/en/latest/index.html
