<script>
    import { Heading, Input, Button } from "flowbite-svelte";
    import { push } from "svelte-spa-router";

    let email = "";
    let password = "";

    const userLoggedIn = () => {
        console.log("Email", email);
        console.log("Password", password);
        push("/dashboard");
    }

    const goToRegister = () => {
        push("/register");
    }
</script>

<Heading tag="h1" class="text-center">Login</Heading>
<br/>
<Input type="email" placeholder="Email" bind:value={email} />
<Input type="password" placeholder="Password" bind:value={password} />
<br/>
<Button on:click={userLoggedIn}>Login</Button>
<Button on:click={goToRegister}>New user ? Register</Button>
