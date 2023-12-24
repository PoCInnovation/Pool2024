<script lang="ts">
    import { Modal, Input, Heading, Button, Star, A } from "flowbite-svelte";
    import type { Artist } from "../types/Artist.svelte";
    import { nanoid } from "nanoid";

    export let openModal:boolean;
    export let artists:Artist[];
    let name = "";
    let rating = 0;
    let nationality = "";
    let musicGender = "";
    let photoUrl = "";
    let ratings = [1, 2, 3, 4, 5];

    const addArtist = (name:string, rating:number,
    nationality:string, musicGender:string, photoUrl:string) => {
        const newArtist:Artist = { id: nanoid(), name: name, rating: rating, nationality: nationality,
            musicGender: musicGender, photoUrl: photoUrl};
        artists = [...artists, newArtist];
        console.log("ARTISTS", artists)
        openModal = false;
    }
</script>

<Modal bind:open={openModal}>
    <Heading tag="h3">Add an artist</Heading>
    <Input type="text" placeholder="Artist's name" bind:value={name}/>
    <Input type="text" placeholder="Artist's nationality" bind:value={nationality}/>
    <Input type="text" placeholder="Artist's music gender" bind:value={musicGender}/>
    <Input type="text" placeholder="Artist's photo url" bind:value={photoUrl}/>
    <p>Rate the artist</p>
    {#each ratings as score, i}
        <A href="/#/dashboard" on:click={() => rating = score }>
            <Star fillPercent={(score <= rating && rating <= 5 && rating >= 0) ? 100 : 0}/>
        </A>
    {/each}
    <br/>
    <Button on:click={() => addArtist(name, rating, nationality, musicGender, photoUrl)}>Add</Button>
</Modal>