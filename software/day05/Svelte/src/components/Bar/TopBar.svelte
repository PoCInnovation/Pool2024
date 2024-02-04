<script lang="ts">
    import { A, NavUl, Navbar } from "flowbite-svelte";
    import type { Artist } from "../../types/Artist.svelte";
    import AddArtistButton from "../Button/AddArtistButton.svelte";

    export let artists:Artist[];
</script>

<Navbar>
    <A href="/#/dashboard">Dashboard</A>
    <NavUl>
        <AddArtistButton artists={artists}/>
    </NavUl>
</Navbar>
