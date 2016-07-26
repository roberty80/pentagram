"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var LoginForm = React.createClass({
	render: function() {
        var style4 = {
            color: 'white'
    };
        var stylea = {
            color: 'white'
    };
        document.body.style.backgroundImage = "url('DOCK-SKY-LAKE-4K-WALLPAPER.jpg')";
        document.body.style.backgroundPosition = "cover";
        return (
			<form>
                
                <br></br>
                <center><h1 style={style4}>Login</h1></center>

                 <br></br> <br></br>
                <label htmlFor="Username" style={style4}>Username:</label>
                <input type="text" name="Username"
                className="form-control"
                placeholder="Username"
                ref="Username"
                />
                <br />

                <label htmlFor="Password" style={style4}>Password:</label>
                <input type="password"
                       name="Password"
                       className="form-control"
                       placeholder="Password"
                       ref="password"
                       />
                <br />

                <input type="submit" value="Login" className="btn btn-default" />

<br></br>
                <br></br>
                <Link to = "Register">
                     <label htmlFor="Register" style={style4}>If you don't have account register here</label>
                    </Link>
                <br></br>
                <Link to = "Home">
                     <label htmlFor="Home" style={style4}>Home</label>
                    </Link>
                <br></br>
                
            </form>

		);
	}
});

module.exports = LoginForm;