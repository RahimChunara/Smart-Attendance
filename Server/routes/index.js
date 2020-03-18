const express = require('express');
const router = express.Router();
const { ensureAuthenticated, forwardAuthenticated } = require('../config/auth');

// Welcome Page
router.get('/', forwardAuthenticated, (req, res) => res.render('login'));

// Dashboard
router.get('/home', ensureAuthenticated, (req, res) =>
  res.render('upload', {
    user: req.user
  })
);

router.get('/portal', ensureAuthenticated, (req, res) =>
  res.render('portal', {
    user: req.user
  })
);
module.exports = router;
