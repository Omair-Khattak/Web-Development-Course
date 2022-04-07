import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class Cal extends Component{
  constructor(){
    super();
    this.state = {
      var1: 20,
      var2: 10,
      result: 0
    }
  }
  add=() => {
    this.setState({result: this.state.var1 + this.state.var2})
    this.setState({var1: this.state.result})
  }  

  sub=() => {
    this.setState({result: this.state.var1 - this.state.var2})
    this.setState({var2: this.state.result})
  }
  

  render(){
    return(
      <>
      <p>First number is: {this.state.var1}</p>
      <p>Second number is: {this.state.var2}</p>
      <button onClick={this.add}>Add</button>
      <button onClick={this.sub}>Subtract</button>
      <p>Result is:{this.state.result}</p>
      </>
    );
  }
}
ReactDOM.render(<Cal/>,document.getElementById('root'));
