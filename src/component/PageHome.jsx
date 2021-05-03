import React from "react";
import "./PageHome.css";
import { Link } from "react-router-dom";
import Loading from "./box/Loading.jsx";
import { getGlobalAppURL, getEcosystemAppURL } from "../utils/env.jsx";

export default class PageHome extends React.Component {
	constructor(props) {
		super(props);

		this.state = {
		};
	}

	render() {
		return (
			<div className={"PageHome page max-sized-page"}>
				<div className={"row"}>
					<div className="col-md-12">
						<h1>Home</h1>
					</div>
				</div>

				<div className={"row row-spaced"}>
					<div className="col-md-12">
						<h2>Visit CYBERSECURITY Luxembourg apps</h2>
					</div>

					<div className="col-md-6">
						<a
							href={getGlobalAppURL()}
							target="_blank"
							rel="noreferrer"
						>
							<div className="PageHome-white-block">
								<img
									src="/img/logo.png"
									alt="CYBERLUX Logo"
								/>
								<h3>CYBERSECURITY Luxembourg</h3>
							</div>
						</a>
					</div>

					<div className="col-md-6">
						<a
							href={getEcosystemAppURL()}
							target="_blank"
							rel="noreferrer"
						>
							<div className="PageHome-white-block">
								<img
									src="/img/logo.png"
									alt="CYBERLUX Logo"
								/>
								<h3>CYBERSECURITY Luxembourg Ecosystem</h3>
							</div>
						</a>
					</div>
				</div>

				<div className={"row row-spaced"}>
					<div className="col-md-12">
						<h2>My profile</h2>

						<a
							onClick={() => this.props.changeMenu("profile")}
						>
							<Link to="/profile">
								<div className="PageHome-white-block">
									<i className="fas fa-user"/>
									<h3>{this.props.email.split("@")[0]}</h3>
								</div>
							</Link>
						</a>
					</div>
				</div>

				<div className={"row row-spaced"}>
					<div className="col-md-12">
						<h2>My entities</h2>
					</div>

					{this.props.myCompanies === null
						&& <Loading
							height={150}
						/>
					}

					{this.props.myCompanies !== null
						&& this.props.myCompanies.length === 0
						&& <div
							className="col-md-12">
							<a
								onClick={() => this.props.changeMenu("add_company")}
							>
								<Link to={"/add_company"}>
									<div className="PageHome-white-block">
										<i className="fas fa-plus-circle"/>
										<h3>No company found, please add or request an entity</h3>
									</div>
								</Link>
							</a>
						</div>
					}

					{this.props.myCompanies !== null
						&& this.props.myCompanies.length > 0
						&& this.props.myCompanies.map((c) => <div
							key={c.id}
							className="col-md-6">
							<a
								onClick={() => this.props.changeMenu("/company/" + c.id)}
							>
								<Link to={"/company/" + c.id}>
									<div className="PageHome-white-block">
										<i className="fas fa-building"/>
										<h3>{c.name}</h3>
									</div>
								</Link>
							</a>
						</div>)
					}
				</div>
			</div>
		);
	}
}
