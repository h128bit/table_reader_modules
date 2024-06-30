<h1> Table reader REST API </h1>

Body all requests must contain key <b>"data"</b>

<h3> Get image with drawed cells</h3>

<code> POST: api/v1/drawcells </code> <br>

In body must contain file (png/jpg/jpeg/pdf) upload from form <br>
<b>return:</b> JSON like {"image": [img1, img2, ...] } <br>
    - where img_i is image encode in base 64 

<h3>Get recognize table</h3>

<code>POST: api/v1/recognize</code>

In body must contain images in bytes <br>
<b>return:</b> JSON like {"table": [table1, table2, ...] } <br>
   - where table_i is {"col1": [val1, val2, ...], "col2": [val1, val2, ...], ...}


<h3>Download table</h3>

<code>POST: api/v1/downloadexcel</code>

In body must contain table in JSON <br>
<b>return:</b> .xlsx file for download