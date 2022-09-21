<template>
  <main>
    <table>
      <thead>
        <tr>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <CartItem
          v-for="item in cart.items"
          :key="item.product.id"
          :item="item"
          @remove="removeFromCart"
        />
      </tbody>
    </table>
    <tr>
      <td>
        <!-- <router-link :to="item.product.get_absolute_url">{{
          item.product.name
        }}</router-link> -->
      </td>
      <td>${{ item.product.price }}</td>
      <td>
        {{ item.quantity }}
        <a @click="decrementQuantity(item)">-</a>
        <a @click="incrementQuantity(item)">+</a>
      </td>
      <td>${{ getItemTotal(item).toFixed(2) }}</td>
      <td>
        <button class="delete" @click="removeFromCart(item)"></button>
      </td>
    </tr>
  </main>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }

      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);

      this.updateCart();
    },
  },
};
</script>

<style>
</style>