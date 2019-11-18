import React from 'react';

import { Form, Input, Button } from 'antd';

import axios from 'axios';

class CustomForm extends React.Component {

  handleFormSubmit = (event, politicianID) => {
  // handleFormSubmit = (event, requestType, politicianID, commentID) => {
    //event.preventDefault();
    const comment = event.target.elements.comment.value;
    console.log(comment);

    //const politicianID2 = this.props.match.params.politicianID;
    // return axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID2}/`, {comment: comment})
    axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
      .then(res => console.log(res))
      .catch(err => console.err(err));

    // switch ( requestType ) {
    //   case 'post':
        // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}`, {comment: comment})
        //   .then(res => console.log(res))
        //   .catch(err => console.err(error));
    //
    //   case 'put':
        // axios.put(`http://127.0.0.1:8000/commentsdetails/${commentID}`, {comment: comment})
        //   .then(res => console.log(res))
        //   .catch(err => console.err(error));
    // }

  }

  // <Form onSubmit={this.handleFormSubmit}>
  // <Form onSubmit={(event) => this.handleFormSubmit(event, this.props.requestType, this.props.politicianID, this.props.commentID)}>
  // <Button type="primary" htmlType="submit">Publicar</Button>
  //<Button type="primary" htmlType="submit">{this.props.btnText}</Button>
  render() {
    return (
      <div>
        <Form onSubmit={(event) => this.handleFormSubmit(event, this.props.politicianID)}
          style={{
            border: '1px solid rgb(235, 237, 240)',
          }}>
          <h2 style={{marginLeft:'20px', marginTop:'10px'}}>Crear un comentario</h2>
          <Form.Item style={{marginLeft:'20px'}} label="Comentario">
            <Input name="comment" placeholder="Ingrese su comentario" />
          </Form.Item>
          <Form.Item>
            <Button style={{marginLeft:'20px'}} type="primary" htmlType="submit">Publicar</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}


export default CustomForm;
