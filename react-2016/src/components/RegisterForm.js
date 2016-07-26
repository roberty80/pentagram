/**
 * Created by Robert Kádár on 25/07/2016.
 */
"use strict";

var React = require('react');
var Router = require('react-router');
var Link = Router.Link;

var RegisterForm = React.createClass({
	render: function() {
        var style2 = {
            color: 'white',
            fontSize: 25,

            textAlignLast: 'center'
            
    };
        var style22 = {
            color: 'white',
            fontSize: 15,

            textAlignLast: 'center'

    };
        var style222 = {
            width: "350px",
        height: "420px",
        margin: 'auto'

    };
        return (
			<form style={style222}>
                <br></br>
                <center><h1 style={style2}>Login</h1></center>

                 <br></br> <br></br>
                <label htmlFor="Username" style={style2}>Username:</label>
                <input type="text" name="Username"
                className="form-control"
                placeholder="Username"
                ref="Username"
                />
                <br />

                <label htmlFor="Password" style={style2}>Password:</label>
                <input type="password"
                       name="Password"
                       className="form-control"
                       placeholder="Password"
                       ref="password"
                       />
                <br />
                <label htmlFor="E-Mail" style={style2}>E-Mail</label>
                <input type="text"
                       name="E-Mail"
                       className="form-control"
                       placeholder="E-Mail"
                       ref="E-Mail"
                       />


<br></br> <br></br>
                <Link to = "Register">
                    <input type="button" value = "Login"/>
                    </Link>
<br></br>
                 <Link to = "Register">
                     <label htmlFor="Register" style={style22}>If you don't have account register here</label>
                    </Link>

            </form>

		);
	}
});

module.exports = RegisterForm;