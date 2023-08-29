import React, { useState } from "react";
import {
  Box,
  Button,
  Card,
  CardContent,
  TextField,
  CardHeader,
  Divider,
  Grid,
  InputAdornment,
  SvgIcon,
  Typography,
  Modal,
} from "@mui/material";
import { Download as DownloadIcon } from "../../icons/download";
import { Search as SearchIcon } from "../../icons/search";
import { Upload as UploadIcon } from "../../icons/upload";
import axios from "axios";
import { baseUrl } from "src/utils/get-initials";

const stores = [
  {
    value: 1,
    name: "FarmFood Arlington",
  },
  {
    value: 2,
    name: "FarmFood_Irving",
  },
  {
    value: 3,
    name: "FarmFood_Dallas",
  },
  {
    value: 4,
    name: "FarmFood_FortWorth",
  },
  {
    value: 5,
    name: "FarmFood_Plano",
  },
];

const category = [
  {
    value: 1,
    name: "DAIRY PRODUCTS",
  },
  {
    value: 2,
    name: "SOFT DRINKS",
  },
  {
    value: 3,
    name: "DAILY NEEDS",
  },
  {
    value: 4,
    name: "WINE",
  },
  {
    value: 5,
    name: "BEER",
  },
  {
    value: 6,
    name: "CHIPS",
  },
  {
    value: 7,
    name: "CANDY",
  },
  {
    value: 8,
    name: "CHOCLATE",
  },
  {
    value: 9,
    name: "COSMETICS",
  },
  {
    value: 10,
    name: "MEDICAL",
  },
  {
    value: 11,
    name: "INSTANT FOOD",
  },
  {
    value: 12,
    name: "ICE CREAM",
  },
  {
    value: 13,
    name: "CAKES",
  },
  {
    value: 14,
    name: "PAPER GOODS",
  },
  {
    value: 15,
    name: "PERSONAL CARE",
  },
  {
    value: 16,
    name: "MEAT",
  },
];

export const ProductListToolbar = (props) => {
  const style = {
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: 400,
    bgcolor: "background.paper",
    border: "2px solid #000",
    boxShadow: 24,
    p: 4,
  };
  const [open, setOpen] = React.useState(false);
  const [title, setTitle] = useState("New Product");
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const initProduct = {
    product_name: "",
    store_name: "",
    product_category: "",
    product_id: "",
    store_id: "1",
    product_category_id: "1",
    cost_price: "0",
    selling_price: "0",
    local_brand: "l",
    inventory: "0",
  };

  const [values, setValues] = useState(initProduct);

  const handleChange = (event) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value,
    });
  };

  const handleCreate = () => {
    console.log(values);
    createProduct(values);
    document.getElementById("createProductForm").reset();
    setOpen(false);
    setValues(initProduct);
  };

  function createProduct(obj) {
    axios({
      url: baseUrl + `products`,
      method: "post",
      data: obj,
    }).then((res) => {
      console.log(res.data);
    });
  }

  return (
    <Box {...props}>
      <Box
        sx={{
          alignItems: "center",
          display: "flex",
          justifyContent: "space-between",
          flexWrap: "wrap",
          m: -1,
        }}
      >
        <Typography sx={{ m: 1 }} variant="h4">
          Products
        </Typography>
        <Box sx={{ m: 1 }}>
          <Button sx={{ m: 1 }} onClick={handleOpen} color="primary" variant="contained">
            Create Product
          </Button>
          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
          >
            <Box sx={style}>
              <form
                autoComplete="off"
                noValidate
                id="createProductForm"
                onSubmit={handleCreate}
                {...props}
              >
                <CardHeader title={title} />
                <Divider />
                <CardContent>
                  <Grid container spacing={3}>
                    <Grid item md={12}>
                      <TextField
                        fullWidth
                        label="Select Store"
                        name="store_id"
                        onChange={handleChange}
                        required
                        select
                        SelectProps={{ native: true }}
                        value={values.store_id}
                        variant="outlined"
                      >
                        {stores.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.name}
                          </option>
                        ))}
                      </TextField>
                    </Grid>
                    <Grid item md={6} xs={12}>
                      <TextField
                        fullWidth
                        label="Select Category"
                        name="product_category_id"
                        onChange={handleChange}
                        required
                        select
                        SelectProps={{ native: true }}
                        value={values.product_category_id}
                        variant="outlined"
                      >
                        {category.map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.name}
                          </option>
                        ))}
                      </TextField>
                    </Grid>
                    <Grid item md={6} xs={12}>
                      <TextField
                        fullWidth
                        label="Select State"
                        name="local_brand"
                        onChange={handleChange}
                        required
                        select
                        SelectProps={{ native: true }}
                        value={values.local_brand}
                        variant="outlined"
                      >
                        {[
                          { value: "l", name: "Local" },
                          { value: "b", name: "Brand" },
                        ].map((option) => (
                          <option key={option.value} value={option.value}>
                            {option.name}
                          </option>
                        ))}
                      </TextField>
                    </Grid>
                    {/* <Grid item>
                      <TextField
                        fullWidth
                        label="Last name"
                        name="lastName"
                        onChange={handleChange}
                        required
                        value={values.lastName}
                        variant="outlined"
                      />
                    </Grid> */}
                    <Grid item md={8} xs={12}>
                      <TextField
                        fullWidth
                        label="Product Name"
                        name="product_name"
                        onChange={handleChange}
                        required
                        value={values.product_name}
                        variant="outlined"
                      />
                    </Grid>
                    <Grid item md={4} xs={12}>
                      <TextField
                        fullWidth
                        label="Qty"
                        name="inventory"
                        onChange={handleChange}
                        type="number"
                        value={values.inventory}
                        variant="outlined"
                      />
                    </Grid>
                    <Grid item md={6} xs={12}>
                      <TextField
                        fullWidth
                        label="Cost Price"
                        name="cost_price"
                        onChange={handleChange}
                        required
                        type="number"
                        value={values.cost_price}
                        variant="outlined"
                      />
                    </Grid>
                    <Grid item md={6} xs={12}>
                      <TextField
                        fullWidth
                        label="Selling Price"
                        name="selling_price"
                        onChange={handleChange}
                        required
                        type="number"
                        value={values.selling_price}
                        variant="outlined"
                      />
                    </Grid>
                  </Grid>
                </CardContent>
                <Divider />
                <Box
                  sx={{
                    display: "flex",
                    justifyContent: "flex-end",
                    p: 2,
                  }}
                >
                  <Button color="primary" variant="contained" type="submit">
                    Create Product
                  </Button>
                </Box>
              </form>
            </Box>
          </Modal>
        </Box>
      </Box>
      {/* <Box sx={{ mt: 3 }}>
      <Card>
        <CardContent>
          <Box sx={{ maxWidth: 500 }}>
            <TextField
              fullWidth
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SvgIcon fontSize="small" color="action">
                      <SearchIcon />
                    </SvgIcon>
                  </InputAdornment>
                ),
              }}
              placeholder="Search product"
              variant="outlined"
            />
          </Box>
        </CardContent>
      </Card>
    </Box> */}
    </Box>
  );
};
