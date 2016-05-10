import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Player } from './player';
import 'rxjs/Rx';

@Injectable()
export class HighScoreService {
    private highScoresUrl = '/highscores';
    
    constructor(private http: Http) {}
    
    // Get overall high score list
    getHighScores(): Observable<Player[]> {
        return this.http.get(this.highScoresUrl)
                        .map(this.extractData)
                        .catch(this.handleError);
    }
    
    private extractData(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        }
        let body = res.json();
        return body.data || { };
    }
    
    private handleError (error: any) {
        let errMsg = error.message || 'Server error';
        console.error(errMsg); // log to console
        return Observable.throw(errMsg);
  }
}