import React from 'react';
import { List, Avatar, Icon, Button } from 'antd';
import axios from 'axios';

class Comments extends React.Component {

  // pagination={{
  //   onChange: page => {
  //     console.log(page);
  //   },
  //   pageSize: 50,
  // }}
  onClick = (id, amount, reaction) => {
    // const comment = event.target.elements.comment.value;
    // console.log(comment);
    // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
    //   .then(res => console.log(res))
    //   .catch(err => console.err(err));

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
  // case 'dislike':
  //   axios.patch(`http://127.0.0.1:8000/commentsdetails/${id}/`, {dislikes: amount+1})
  //   .then(res => console.log(res))
  //   .catch(err => console.error(err));

  // console.log("ss")

  // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
  //   .then(res => console.log(res))
  //   .catch(err => console.err(err));

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










//
// Comments.js
// v1
//
// import React from 'react';
// import { List, Avatar, Icon } from 'antd';
//
// const IconText = ({ type, text }) => (
//   <span>
//     <Icon type={type} style={{ marginRight: 8 }} />
//     {text}
//   </span>
// );
//
//
// const Comments = (props) => {
//   return(
//     <List
//       itemLayout="vertical"
//       size="large"
//       // pagination={{
//       //   onChange: page => {
//       //     console.log(page);
//       //   },
//       //   pageSize: 50,
//       // }}
//       dataSource={props.data}
//       renderItem={item => (
//         <List.Item
//           key={item.title}
//           actions={[
//             <IconText type="like-o" text={item.id} key="list-vertical-like-o" />,
//             <IconText type="dislike-o" text={item.dislikes} key="list-vertical-dislike-o" />,
//           ]}
//         >
//           <List.Item.Meta
//             title={item.comm_content}
//             description={item.description}
//           />
//           {item.content}
//         </List.Item>
//       )}
//     />
//   )
// }
//
// export default Comments;
//
//
//
//
// v2
// import React from 'react';
// import { List, Avatar, Icon, Button } from 'antd';
// import axios from 'axios';
//
// class Comments extends React.Component {
//
//   // pagination={{
//   //   onChange: page => {
//   //     console.log(page);
//   //   },
//   //   pageSize: 50,
//   // }}
//   onClick() {
//     // const comment = event.target.elements.comment.value;
//     // console.log(comment);
//     // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
//     //   .then(res => console.log(res))
//     //   .catch(err => console.err(err));
//
//
//     console.log("ss")
//     // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
//     //   .then(res => console.log(res))
//     //   .catch(err => console.err(err));
//   }
//
//
//   render() {
//     const IconText = ({ type, text, icon }) => (
//       <span>
//         <Button type={type} icon={icon} size="large" onClick={() => this.onClick() }>{text}</Button>
//       </span>
//     );
//
//
//     return(
//       <List
//         itemLayout="vertical"
//         size="large"
//         dataSource={this.props.data}
//         renderItem={item => (
//           <List.Item
//             key={item.title}
//             actions={[
//               <IconText type="primary" text={" "+ item.likes} icon="like-o" key="list-vertical-like-o"  />,
//               <IconText type="danger" text={" "+ item.dislikes} icon="dislike-o" key="list-vertical-dislike-o" />,
//             ]}
//           >
//             <List.Item.Meta
//               title={item.comm_content}
//               description={item.description}
//
//             />
//             {item.content}
//           </List.Item>
//         )}
//       />
//     )
//   }
//
// }
//
// export default Comments;
//
//
//
// v3
// import React from 'react';
// import { List, Avatar, Icon, Button } from 'antd';
// import axios from 'axios';
//
// class Comments extends React.Component {
//
//   // pagination={{
//   //   onChange: page => {
//   //     console.log(page);
//   //   },
//   //   pageSize: 50,
//   // }}
//   onClick = (column) => {
//     // const comment = event.target.elements.comment.value;
//     // console.log(comment);
//     // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
//     //   .then(res => console.log(res))
//     //   .catch(err => console.err(err));
//
//
//     // console.log("ss")
//     console.log(column)
//     // axios.post(`http://127.0.0.1:8000/politiciansdetails/${politicianID}/`, {comm_content: comment})
//     //   .then(res => console.log(res))
//     //   .catch(err => console.err(err));
//   }
//
//
//   render() {
//     const IconText = ({ type, text, icon }) => (
//       <span>
//         <Button type={type} icon={icon} size="large" onClick={() => this.onClick("pepe") }>{text}</Button>
//       </span>
//     );
//
//
//     return(
//       <List
//         itemLayout="vertical"
//         size="large"
//         dataSource={this.props.data}
//         renderItem={item => (
//           <List.Item
//             key={item.title}
//             actions={[
//               <IconText type="primary" text={" "+ item.likes} icon="like-o" key="list-vertical-like-o"  />,
//               <IconText type="danger" text={" "+ item.dislikes} icon="dislike-o" key="list-vertical-dislike-o" />,
//             ]}
//           >
//             <List.Item.Meta
//               title={item.comm_content}
//               description={item.description}
//
//             />
//             {item.content}
//           </List.Item>
//         )}
//       />
//     )
//   }
//
// }
//
// export default Comments;
