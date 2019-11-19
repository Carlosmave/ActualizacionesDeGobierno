import React from 'react';
import axios from 'axios';
import { PageHeader } from 'antd';
import Politicians from '../components/Politicians';

class ProvinceDetail extends React.Component {


  state = {
      politicians: [],
      province: {},
    }


  componentDidMount() {
    const provinceID = this.props.match.params.provinceID;
    axios.get(`http://127.0.0.1:8000/locationpoliticians/${provinceID}/`)
        .then(res => {
            this.setState({
              politicians: res.data
            });
            console.log(res.data);
        })
    axios.get(`http://127.0.0.1:8000/provinces/${provinceID}/`)
        .then(res => {
            this.setState({
              province: res.data
            });
            console.log(res.data);
        })

  }

  render() {
    return(
      <div>
      <PageHeader
        style={{
          border: '1px solid rgb(235, 237, 240)',
        }}
        title= {"Actuales Autoridades Provinciales de " + this.state.province.prov_name}
      />
      <br />
      <Politicians data={this.state.politicians} />
      </div>

    )
  }
}

export default ProvinceDetail
