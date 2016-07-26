"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var HomeForm = React.createClass({
	render: function() {
        var style3 = {
      color: 'white',
      fontSize: 20
    };
        return (
			<form>
                <br></br>
                <center style={style3}><h1>HOME</h1></center>


                 <br></br> <br></br> <br></br> <br></br>
                
                <center style={style3}><h1>BINE ATI VENIT!</h1></center>


            </form>

		);
	}
});

module.exports = HomeForm;
