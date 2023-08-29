import PropTypes from "prop-types";
import {
  Avatar,
  Box,
  Card,
  CardContent,
  Divider,
  TextField,
  InputAdornment,
  SvgIcon,
  Button,
  IconButton,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import PerfectScrollbar from "react-perfect-scrollbar";
import { Clock as ClockIcon } from "../../icons/clock";
import { Download as DownloadIcon } from "../../icons/download";
import React, { useEffect, useState } from "react";
import { Search as SearchIcon } from "../../icons/search";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import axios from "axios";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { baseUrl } from "src/utils/get-initials";

export const ProductCard = ({
  store_id,
  product,
  productParentCallback,
  productvalues,
  searchParentCallback,
  ...rest
}) => {
  const [selectedCustomerIds, setSelectedCustomerIds] = useState([]);
  const [limit, setLimit] = useState(10);
  const [page, setPage] = useState(0);

  const [open, setOpen] = React.useState(false);

  const [delItem, setDelItem] = useState({});

  const handleClickOpen = (obj) => {
    setDelItem(obj);
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const columns = [
    {
      field: "store_name",
      headerName: "Store name",
      flex: 1,
      editable: true,
    },
    {
      field: "product_name",
      headerName: "Product name",
      flex: 1,
      editable: true,
    },
    {
      field: "product_category",
      headerName: "Product Category",
      type: "singleSelect",
      valueOptions: [
        "DAIRY PRODUCTS",
        "SOFT DRINKS",
        "DAILY NEEDS",
        "WINE",
        "BEER",
        "CHIPS",
        "CANDY",
        "CHOCLATE",
        "COSMETICS",
        "MEDICAL",
        "INSTANT FOOD",
        "ICE CREAM",
        "CAKES",
        "PAPER GOODS",
        "PERSONAL CARE",
        "MEAT",
      ],
      flex: 1,
      editable: true,
    },
    {
      field: "inventory",
      headerName: "Inventory",
      sortable: true,
      flex: 1,
      editable: true,
    },
    {
      field: "cost_price",
      headerName: "Cost Price",
      sortable: true,
      flex: 1,
      editable: true,
    },
    {
      field: "selling_price",
      headerName: "Selling Price",
      sortable: true,
      flex: 1,
      editable: true,
    },
    {
      field: "actions",
      headerName: "Action",
      type: "actions",
      width: 100,
      renderCell: (params) => {
        return (
          <strong>
            <Button
              color="error"
              startIcon={<DeleteIcon />}
              onClick={() => {
                const obj = params.row;
                obj.status = 0;

                // console.log(obj);

                handleClickOpen(obj);
              }}
            />
          </strong>
        );
      },
    },
  ];

  var rows = productvalues;

  const handleSearchChange = (event) => {
    var val = event.target.value;
    if (val.length >= 3) {
      searchParentCallback(val);
    } else {
      searchParentCallback(0);
    }
  };

  const updateProduct = (obj) => {
    axios({
      url: baseUrl + `products`,
      method: "put",
      data: obj,
    }).then((res) => {
      // console.log(res.data);
      handleClose();
    });
  };

  return (
    <Card
      sx={{
        display: "flex",
        flexDirection: "column",
        height: "100%",
      }}
      {...rest}
    >
      <Card {...rest}>
        <PerfectScrollbar>
          <Box sx={{ width: "100%", height: 500 }}>
            <Box sx={{ mt: 3 }}>
              <Card>
                <CardContent>
                  <Box sx={{ maxWidth: 500 }}>
                    <TextField
                      onChange={handleSearchChange}
                      fullWidth
                      InputProps={{
                        startAdornment: (
                          <InputAdornment position="start">
                            <SvgIcon color="action" fontSize="small">
                              <SearchIcon />
                            </SvgIcon>
                          </InputAdornment>
                        ),
                      }}
                      placeholder="Search customer"
                      variant="outlined"
                    />
                  </Box>
                </CardContent>
              </Card>
            </Box>
            <Dialog
              open={open}
              onClose={handleClose}
              aria-labelledby="alert-dialog-title"
              aria-describedby="alert-dialog-description"
            >
              <DialogTitle id="alert-dialog-title">{"Warning - Alert!"}</DialogTitle>
              <DialogContent>
                <DialogContentText id="alert-dialog-description">
                  Are you sure you want to delete this product?
                </DialogContentText>
              </DialogContent>
              <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={() => updateProduct(delItem)}>Delete</Button>
              </DialogActions>
            </Dialog>
            <DataGrid
              sx={{ textAlign: "center" }}
              rows={rows}
              columns={columns}
              pageSize={10}
              getRowId={(row) => row.product_id}
              disableColumnMenu={true}
              onCellEditStop={(params, event) => {
                const product = params.row;
                product[params.field] = event.target.value;

                updateProduct(product);
              }}
            />
          </Box>
        </PerfectScrollbar>
      </Card>
      <Box sx={{ flexGrow: 1 }} />
      <Divider />
    </Card>
  );
};

ProductCard.propTypes = {
  product: PropTypes.object.isRequired,
};
