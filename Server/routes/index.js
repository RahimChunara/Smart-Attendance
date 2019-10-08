const express = require('express');
const router = express.Router();
const { ensureAuthenticated, forwardAuthenticated } = require('../config/auth');

// Welcome Page
router.get('/', forwardAuthenticated, (req, res) => res.render('login'));

// Dashboard
router.get('/upload', ensureAuthenticated, (req, res) =>
  res.render('upload', {
    user: req.user
  })
);

module.exports = router;
