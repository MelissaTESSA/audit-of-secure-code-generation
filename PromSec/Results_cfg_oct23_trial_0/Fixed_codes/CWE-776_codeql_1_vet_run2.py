function upload(req, res) {
  const xmlData = req.body;
  
  // Process XML data here
  
  res.status(200).send('XML data processed successfully');
}