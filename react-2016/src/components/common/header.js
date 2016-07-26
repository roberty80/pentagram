"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var Header = React.createClass({
	render: function() {
        var style = {
            backgroundColor: 'powderblue'
            };
        var style2 = {
            backgroundColor: 'pink'
            };

		return (

        <nav className="navbar navbar-default">


          <div className="container-fluid" style={style}>
              <ul className="nav navbar-nav" >
                <li><Link to="app">Home</Link></li>
                <li><Link to="about">About</Link></li>
              </ul>
          </div>
        </nav>
		);
	}
});

module.exports = Header;
