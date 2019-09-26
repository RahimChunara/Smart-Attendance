var express = require('express');
var router = express.Router();
var User = require('../models/user');


// GET route for reading data
router.get('/', function (req, res, next) {
  return res.sendFile(path.join(__dirname + '/Views/index.html'));
});


//POST route for updating data
router.post('/', function (req, res, next) {

  var userData = {
    username: 'universe',
    password: 'universe',
  }

  User.create(userData, function (error, user) {
    if (error) {
      return next(error);
    } else {
      req.session.userId = user._id;
      return res.redirect('/home.html');
    }
  });

  if (req.body.username && req.body.password) {
    User.authenticate(req.body.username, req.body.password, function (error, user) {
      if (error || !user) {
        var err = new Error('Wrong email or password.');
        err.status = 401;
        return next(err);
      } else {
        req.session.userId = user._id;
        return res.redirect('/home.html');
      }
    });
  } else {
    var err = new Error('All fields required.');
    err.status = 400;
    return next(err);
  }
})

// GET for logout logout
router.get('/logout', function (req, res, next) {
  if (req.session) {
    // delete session object
    req.session.destroy(function (err) {
      if (err) {
        return next(err);
      } else {
        return res.redirect('/');
      }
    });
  }
});

module.exports = router;