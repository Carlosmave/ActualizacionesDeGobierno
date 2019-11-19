import React from 'react';
import axios from 'axios';
import { PageHeader, Menu, Icon, Input } from 'antd';
import Politicians from '../components/Politicians';
import Provinces from '../components/Provinces';

class RegionDetail extends React.Component {


  state = {
      politicians: [],
      region: {},
      regionprovinces: [],
      current: 'provinces',
      search: ""
    }

  handleClick = e => {
    console.log('click ', e);
    this.setState({
      current: e.key,
    });
  };

  onChange = e => {
    this.setState({ search: e.target.value });
  };

  componentDidMount() {
    const regionID = this.props.match.params.regionID;
    axios.get(`http://127.0.0.1:8000/locationpoliticians/${regionID}/`)
        .then(res => {
            this.setState({
              politicians: res.data
            });
            console.log(res.data);
        })
    axios.get(`http://127.0.0.1:8000/regions/${regionID}/`)
        .then(res => {
            this.setState({
              region: res.data
            });
            console.log(res.data);
        })
    axios.get(`http://127.0.0.1:8000/regionprovinces/${regionID}/`)
        .then(res => {
            this.setState({
              regionprovinces: res.data
            });
            console.log(res.data);
        })

  }

  render() {
    let content
    const selection = this.state.current
    const search = this.state.search;
    const filteredProvinces = this.state.regionprovinces.filter(province => {
      return province.prov_name.toLowerCase().indexOf(search.toLowerCase()) !== -1;
    });
    const { Search } = Input;

    if (selection==="provinces") {
      content =       <div>
                        <PageHeader
                          style={{
                            border: '1px solid rgb(235, 237, 240)',
                          }}
                          title= {"Provincias de " + this.state.region.reg_name}
                        />
                        <br />
                        <Search
                          placeholder="Buscar provincia"
                          onChange={this.onChange}
                        />
                        <br />
                        <br />

                        <Provinces data={filteredProvinces} />
                      </div>;
    } else if (selection==="authorities"){
      content =       <div>
                        <PageHeader
                          style={{
                            border: '1px solid rgb(235, 237, 240)',
                          }}
                          title= {"Actuales Autoridades Regionales de " + this.state.region.reg_name}
                        />
                        <br />
                        <Politicians data={this.state.politicians} />
                      </div>;
    }

    return(
      <div>
      <Menu onClick={this.handleClick} selectedKeys={[this.state.current]} mode="horizontal">
        <Menu.Item key="provinces">
          <Icon type="global" />
          Provincias
        </Menu.Item>
        <Menu.Item key="authorities">
          <Icon type="user" />
            Autoridades
        </Menu.Item>
      </Menu>
      {content}
      </div>


    )
  }
}

export default RegionDetail
