"use strict";

var React = require('react');

var About = React.createClass({
	render: function () {
		var style = StyleSheet.create({
            container: {
                color: 'white',
                fontsize: 30
            },
            container2: {
                width: "290px",
                height: "330px"
            }
        });
		return (
			<div>
				<h1>About</h1>
				<p>
					This application uses the following technologies:
					<ul>
						<li style={style.container}>React</li>
						<li>React Router</li>
						<li>Flux</li>
						<li>Node</li>
						<li>Gulp</li>
						<li>Browserify</li>
						<li>Bootstrap</li>
					</ul>
				</p>
			</div>
		); 
	}
});

module.exports = About;