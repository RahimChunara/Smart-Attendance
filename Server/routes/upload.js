// var express  = require('express');
// var router = express.Router();
// const bodyParser = require('body-parser');
// const path = require('path');
// const crypto = require('crypto');
// const mongoose = require('mongoose');
// const multer = require('multer');
// const GridFsStorage = require('multer-gridfs-storage');
// const Grid = require('gridfs-stream');
// const methodOverride = require('method-override');

// // Middleware
// router.use(bodyParser.json());
// router.use(methodOverride('_method'));

// // Mongo URI
// const mongoURI = 'mongodb://localhost/IEEEProject';

// // Create mongo connection
// const conn = mongoose.createConnection(mongoURI);

// let gfs;

// conn.once('open', () => {
//   // Init stream
//   gfs = Grid(conn.db, mongoose.mongo);
//   gfs.collection('uploads');
// });

// // Create storage engine
// const storage = new GridFsStorage({
//     url: mongoURI,    
//     file: (req, file) => {
//       return new Promise((resolve, reject) => {
//         crypto.randomBytes(16, (err, buf) => {
//           if (err) {
//             return reject(err);
//           }
//           const filename = buf.toString('hex') + path.extname(file.originalname);
//           const fileInfo = {
//             filename: filename,
//             bucketName: 'uploads'
//           };
//           resolve(fileInfo);
//         });
//       });
//     }
//   });
//   const upload = multer({ storage });

//   // @route GET /
// // @desc Loads form
// router.get('/', (req, res) => {
//     gfs.files.find().toArray((err, files) => {
//       // Check if files
//       if (!files || files.length === 0) {
//         res.render('index', { files: false });
//       } else {
//         files.map(file => {
//           if (
//             file.contentType === 'image/jpeg' ||
//             file.contentType === 'image/png'
//           ) {
//             file.isImage = true;
//           } else {
//             file.isImage = false;
//           }
//         });
//         res.render('index', { files: files });
//       }
//     });
//   });

//   router.post('/upload', upload.single('file'), (req, res) => {
//     res.json({ file: req.file });
//     // res.redirect('/');
//   });