describe('Good front for Register page', () => {
	it('Go to register page', () => {
		cy.visit('/register');
	});

	beforeEach(() => {
		cy.visit('/register');
	});

	it('Good number of buttons', () => {
		cy.get('button').should('have.length', 2);
	});

	it('Good number of inputs', () => {
		cy.get('input').should('have.length', 3);
	});

	it('Good name for register button', () => {
		cy.get('#registerPage-register-button').should('contain', 'Register');
	});

	it('Good name for login button', () => {
		cy.get('#registerPage-login-button').should('contain', 'Already a user ? Login');
	});
});

describe('Login button in register page', () => {
	it('Go to register page', () => {
		cy.visit('/register');
	});

	beforeEach(() => {
		cy.visit('/register');
	});

	it('Good URL redirect for login button', () => {
		cy.get('#registerPage-login-button').click().url().should('eq', `${Cypress.config().baseUrl}/login`);
	});
});
