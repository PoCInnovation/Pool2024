<script>
    import { push } from "svelte-spa-router";

    let email = "";
    let password = "";

    const userLoggedIn = () => {
        console.log("Email", email);
        console.log("Password", password);
    }

    const goToRegister = () => {
        push("/register");
    }
</script>

<h1>Login</h1>
<input type="email" placeholder="Email" bind:value={email}>
<input type="password" placeholder="Password" bind:value={password}>
<button on:click={userLoggedIn}>Login</button>
<button on:click={goToRegister}>New user ? Register</button>