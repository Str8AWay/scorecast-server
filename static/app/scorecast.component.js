"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var high_scores_component_1 = require('./high-scores.component');
var ScorecastComponent = (function () {
    function ScorecastComponent() {
    }
    ScorecastComponent = __decorate([
        core_1.Component({
            selector: 'scorecast',
            template: "\n        <h1>Scorecast</h1>\n        <high-scores></high-scores>\n    ",
            directives: [high_scores_component_1.HighScoresComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], ScorecastComponent);
    return ScorecastComponent;
}());
exports.ScorecastComponent = ScorecastComponent;
//# sourceMappingURL=scorecast.component.js.map