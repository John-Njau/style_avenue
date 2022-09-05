<template>
    <main>
        <Cart/>
    </main>
  
</template>

<script>
import Cart from "@/components/Cart/Cart.vue";

export default {
    name: "CartView",
    components: {
        Cart,
    },
    data() {
        return {
        title: "Cart | Style Avenue Studio",
        };
    },
    mounted() {
        document.title = this.title;
    },
    

}
</script>

<style>

</style>