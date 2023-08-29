import PropTypes from "prop-types";
import styled from "@emotion/styled";
import MenuItem from "@mui/material/MenuItem";
import {
  AppBar,
  Avatar,
  Badge,
  Box,
  IconButton,
  Toolbar,
  Tooltip,
  CardHeader,
  Button,
  Select,
} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import { UserCircle as UserCircleIcon } from "../icons/user-circle";
import { useState } from "react";

const DashboardNavbarRoot = styled(AppBar)(({ theme }) => ({
  backgroundColor: theme.palette.background.paper,
  boxShadow: theme.shadows[3],
}));

export const DashboardNavbar = (props) => {
  const { handleCallback, onSidebarOpen, ...other } = props;

  const [val, setVal] = useState("all");

  const handleStoreChange = (e) => {
    const storeVal = e.target.value;
    setVal(storeVal);
    handleCallback(storeVal)
  };

  return (
    <>
      <DashboardNavbarRoot
        sx={{
          left: {
            lg: 280,
          },
          width: {
            lg: "calc(100% - 280px)",
          },
        }}
        {...other}
      >
        <Toolbar
          disableGutters
          sx={{
            minHeight: 64,
            left: 0,
            px: 2,
          }}
        >
          {/* <CardHeader
            sx={{
              float: "right",
            }}
            action={ */}
          <Select
            labelId="demo-simple-select-standard-label"
            id="demo-simple-select-standard"
            value={val}
            label="Age"
            sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold", outline: "0" }}
            onChange={handleStoreChange}
          >
            <MenuItem
              value={"all"}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              All Stores
            </MenuItem>
            <MenuItem
              value={1}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              FarmFoods - Arlington
            </MenuItem>
            <MenuItem
              value={2}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              FarmFoods - Irving
            </MenuItem>
            <MenuItem
              value={3}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              FarmFoods - Dallas
            </MenuItem>
            <MenuItem
              value={4}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              FarmFoods - FortWorth
            </MenuItem>
            <MenuItem
              value={5}
              sx={{ color: "darkviolet", fontSize: "small", fontWeight: "bold" }}
            >
              FarmFoods - Plano
            </MenuItem>
            
          </Select>

          {/* }
            title="Latest Sales"
          /> */}

          <Box sx={{ flexGrow: 1 }} />
          <Avatar
            sx={{
              height: 40,
              width: 40,
              ml: 1,
              float: "right",
            }}
            src="/static/images/avatars/avatar_1.png"
          >
            <UserCircleIcon fontSize="small" />
          </Avatar>
        </Toolbar>
      </DashboardNavbarRoot>
    </>
  );
};

DashboardNavbar.propTypes = {
  onSidebarOpen: PropTypes.func,
  handleCallback: PropTypes.func,
};
