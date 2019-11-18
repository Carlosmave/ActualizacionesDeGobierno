import React from 'react';
import { List, Button } from 'antd';
import axios from 'axios';

class Comments extends React.Component {

  onClick = (id, amount, reaction) => {

    switch (reaction) {
      case "like":
        axios.patch(`http://127.0.0.1:8000/commentsdetails/${id}/`, {likes: amount+1})
          .then(res => console.log(res))
          .catch(err => console.error(err))
          break;
      case "dislike":
        axios.patch(`http://127.0.0.1:8000/commentsdetails/${id}/`, {dislikes: amount+1})
          .then(res => console.log(res))
          .catch(err => console.error(err))
          break;
    }
    console.log(id, amount, reaction)
    window.location.reload()

  }


  render() {
    return(
      <List
        itemLayout="vertical"
        size="large"
        dataSource={this.props.data}
        renderItem={item => (
          <List.Item
            key={item.title}
            actions={[

              <Button style={{marginLeft:'20px'}} type="primary" icon="like-o" size="large" key="list-vertical-like-o" onClick={() => this.onClick(item.id,item.likes,"like") }>{" "+ item.likes}</Button>,
              <Button type="danger" icon="dislike-o" size="large" key="list-vertical-dislike-o" onClick={() => this.onClick(item.id,item.dislikes,"dislike") }>{" "+ item.dislikes}</Button>,
            ]} style={{border: '1px solid rgb(235, 237, 240)', textAlign:'center'}}
          >
            <List.Item.Meta
              style={{marginLeft:'20px'}}
              title={item.comm_content}
              description={item.description}

            />
            {item.content}
          </List.Item>
        )}
      />
    )
  }
}

export default Comments;
