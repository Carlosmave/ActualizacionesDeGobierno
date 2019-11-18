import React from 'react';

import { Form, Input, Button } from 'antd';

import axios from 'axios';

class CustomForm extends React.Component {

  handleFormSubmit = (event, politicianID) => {

    const comment = event.target.elements.comment.value;
    console.log(comment);
    axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
      .then(res => console.log(res))
      .catch(err => console.err(err));

  }

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
